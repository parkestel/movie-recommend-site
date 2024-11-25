from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model


from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .serializers import VocaNoteSerializers, VocaNoteAllSerializers, VocaSerializers
from .models import VocaNote, Voca, VocaNoteHistory
from movies.models import Movie

User = get_user_model()

# create(내 단어장 로그인한 사용자랑 pk확인), read(다른 사람들 단어장 읽는), update(내 단어장 로그인한 사용자랑 pk확인), delete(내 단어장 로그인한 사용자랑 pk확인)


# Vocanote 생성 : 보는 사람이랑 로그인한 사용자랑 같아야 단어장 생성 가능.
@api_view(["GET", "POST", "DELETE"])  # 로그인된 사용자만 접근 가능
def create_voca_note(request, movie_pk, user_pk):

    person = get_object_or_404(User, pk=user_pk)
    movie = get_object_or_404(Movie, pk=movie_pk)
    me = request.user

    if request.method == "GET":

        voca_notes = VocaNote.objects.filter(users=person, movies=movie)
        if not voca_notes.exists():
            return Response(
                {"error": "해당 영화에 대한 단어장이 없습니다."}, status=404
            )

        if person != me and not any(note.is_public for note in voca_notes):
            return Response({"error": "해당 단어장은 비공개 상태입니다."}, status=403)

        serializer = VocaNoteSerializers(voca_notes, many=True)
        return Response(serializer.data, status=200)

    elif request.method == "POST":

        if me != person:
            return Response(
                {"error": "자신의 단어장만 생성할 수 있습니다."}, status=403
            )

        existing_note = VocaNote.objects.filter(users=me, movies=movie).first()
        if existing_note:
            return Response(
                {"error": "이미 해당 영화에 대한 단어장이 존재합니다."}, status=400
            )

        voca_note = VocaNote.objects.create(is_public=True)  # 기본 공개 상태로 생성
        voca_note.users.add(me)
        voca_note.movies.add(movie)
        voca_note.save()

        VocaNoteHistory.objects.create(user=me, movie=movie)

        if not VocaNoteHistory.objects.filter(user=me, movie=movie).exists():
            me.experience += 500
            me.user.save()

        serializer = VocaNoteSerializers(voca_note)
        return Response(serializer.data, status=201)

    elif request.method == "DELETE":
        # 삭제 - 로그인한 사용자만 가능
        voca_note = VocaNote.objects.filter(users=me, movies=movie).first()
        if not voca_note:
            return Response({"error": "삭제할 단어장이 존재하지 않습니다."}, status=404)

        voca_note.delete()
        return Response({"message": "단어장이 삭제되었습니다."}, status=200)


# 사용자가 is_public 버튼 누르면 그 전값과 반대로 바꿔서 저장.
@api_view(["PUT"])
def change_is_public(request, movie_pk, user_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    person = get_object_or_404(User, pk=user_pk)
    login_user = request.user

    if login_user != person:
        return Response({"error": "자신의 단어장만 수정할 수 있습니다."}, status=403)

    voca_note = VocaNote.objects.filter(users=login_user, movies=movie).first()
    if not voca_note:
        return Response({"error": "수정할 단어장이 존재하지 않습니다."}, status=404)

    voca_note.is_public = not voca_note.is_public
    serializer = VocaNoteSerializers(
        voca_note, data={"is_public": voca_note.is_public}, partial=True
    )
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)


# 사용자 별 VocaNote 전체 리스트 조회
# 만약 로그인
@api_view(["GET"])
def voca_note_list(request, user_pk):

    person = get_object_or_404(User, pk=user_pk)
    login_user = request.user
    voca_notes = None

    # 로그인한 유저랑 user_pk 다르면 is_public = True인 단어장 담아서 조회
    if login_user != person:
        voca_notes = VocaNote.objects.filter(users=person, is_public=True)

    # 로그인한 유저랑 user_pk 같으며 내꺼니까
    else:
        # 전체 voca_notes 리스트 조회
        voca_notes = VocaNote.objects.filter(users=login_user).all()
    if voca_notes is None:
        return Response({"error": "단어장 데이터를 불러올 수 없습니다."}, status=500)

    serializer = VocaNoteSerializers(voca_notes, many=True)
    return Response(serializer.data, status=200)


# 단어 생성
@api_view(["POST"])
def create_voca(request, vocanote_pk):

    voca_note = get_object_or_404(VocaNote, pk=vocanote_pk)

    voca_data = request.data
    print(f"현재 유저 ID: {request.user.pk}")
    print(f"단어장 유저 IDs: {[user.pk for user in voca_note.users.all()]}")
    print(f"Authorization 헤더: {request.headers.get('Authorization')}")

    if not voca_data:
        return Response(
            {"error": "voca 키 또는 값이 비어 있습니다."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    if not voca_note.users.filter(pk=request.user.pk).exists():
        return Response(
            {"error": "해당 단어장에 대해 권한이 없습니다."},
            status=status.HTTP_403_FORBIDDEN,
        )

    # Voca 생성
    voca = Voca.objects.create(
        word=voca_data.get("word"),
        word_mean=voca_data.get("word_mean"),
        examples=voca_data.get("examples"),
        memo=voca_data.get("memo"),
    )

    # 해당 단어장에 voca 저장
    voca_note.vocas.add(voca)
    voca_note.save()

    request.user.experience += 50
    request.user.save()

    serializer = VocaNoteAllSerializers(voca_note)

    return Response(
        {"message": "단어가 성공적으로 추가되었습니다.", "voca_note": serializer.data},
        status=status.HTTP_201_CREATED,
    )


# 단어장 별 전체 정보 조회
@api_view(["GET"])
def voca_note_detail(request, vocanote_pk):
    login_user = request.user
    voca_note = get_object_or_404(VocaNote, pk=vocanote_pk)

    if voca_note.users.filter(pk=login_user.pk).exists():
        serializer = VocaNoteAllSerializers(voca_note)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if not voca_note.is_public:
        return Response(
            {"detail": "해당 단어장의 사용자가 비공개 처리 해놨습니다."},
            status=status.HTTP_403_FORBIDDEN,
        )

    # is_public이 True일 경우 정보 제공
    serializer = VocaNoteAllSerializers(voca_note)
    return Response(serializer.data, status=status.HTTP_200_OK)


# 단어 수정 후 해당 단어장 전체 데이터 반환
@api_view(["PUT"])
def update_voca(request, vocanote_pk, voca_pk):

    login_user = request.user

    voca_note = get_object_or_404(VocaNote, pk=vocanote_pk)
    voca = get_object_or_404(Voca, pk=voca_pk)

    if not voca_note.users.filter(pk=login_user.pk).exists():
        return Response(
            {"error": "해당 단어장에 대해 권한이 없습니다."},
            status=status.HTTP_403_FORBIDDEN,
        )

    # Voca 수정
    serializer = VocaSerializers(voca, data=request.data, partial=True)
    if serializer.is_valid(raise_exception=True):
        serializer.save()

    # 수정 후 전체 단어장 정보 반환
    voca_note.refresh_from_db()  # 단어장 데이터를 새로 고침
    voca_note_serializer = VocaNoteAllSerializers(voca_note)

    return Response(
        {
            "message": "단어가 성공적으로 수정되었습니다.",
            "voca_note": voca_note_serializer.data,
        },
        status=status.HTTP_200_OK,
    )


@api_view(["DELETE"])
def delete_voca(request, vocanote_pk, voca_pk):

    voca_note = get_object_or_404(VocaNote, pk=vocanote_pk)
    voca = get_object_or_404(Voca, pk=voca_pk)

    if not voca_note.users.filter(pk=request.user.pk).exists():
        return Response(
            {"error": "해당 단어장에 대한 권한이 없습니다."},
            status=status.HTTP_403_FORBIDDEN,
        )

    # 단어 삭제
    voca_note.vocas.remove(voca)
    voca.delete()  # 단어 자체 삭제

    # 삭제 후 단어장 정보 갱신
    voca_note.refresh_from_db()
    serializer = VocaNoteAllSerializers(voca_note)

    # 전체 단어장 정보 반환
    return Response(
        {
            "message": "단어가 성공적으로 삭제되었습니다.",
            "voca_note": serializer.data,  # 삭제 후 갱신된 단어장 정보
        },
        status=status.HTTP_200_OK,
    )


@api_view(["POST"])
def change_is_memorized(request, vocanote_pk, voca_pk):

    voca_note = get_object_or_404(VocaNote, pk=vocanote_pk)
    voca = get_object_or_404(Voca, pk=voca_pk)
    login_user = request.user

    if not voca_note.users.filter(pk=login_user.pk).exists():
        return Response(
            {"error": "자신의 단어장 단어들만 수정할 수 있습니다."}, status=403
        )

    if not voca_note:
        return Response({"error": "수정할 단어가 존재하지 않습니다."}, status=404)

    memorized_status = voca.is_memorized
    voca.is_memorized = not voca.is_memorized

    if voca.is_memorized and not voca.was_memorized:
        # 처음 외운 경우 경험치 추가 및 상태 업데이트
        login_user.experience += 70
        login_user.save()
        voca.was_memorized = True
    voca.save()

    if memorized_status:
        message = f"아직 voca{voca.pk}:{voca.word}를 덜 외웠어요."
    else:
        message = f"voca{voca.pk}:{voca.word} 단어를 외웠어요!"

    voca_note.refresh_from_db()
    serializer = VocaNoteAllSerializers(voca_note)

    return Response(
        {"message": message, "voca_note": serializer.data}, status=status.HTTP_200_OK
    )
