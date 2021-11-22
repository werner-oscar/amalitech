

from rest_framework.exceptions import AuthenticationFailed
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from .serializers import DetectFaceSerializer
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import cv2
from django.conf import settings
import os
import face_recognition


class DetectFace(APIView):
	permission_classes = [permissions.AllowAny]
	serializer_class = DetectFaceSerializer

	images_base_path = os.path.join(settings.BASE_DIR,"data")

	def post(self,request):
		serilized = self.serializer_class(data=request.data)
		serilized.is_valid(raise_exception=True)
		image = serilized.validated_data.get("image")
		data = default_storage.save("tmp/face.jpg",ContentFile(image.read()))

		path = os.path.join(settings.MEDIA_ROOT,data)
		read = face_recognition.load_image_file(path)


		try:
			unkown_encoded = face_recognition.face_encodings(read)[0]
		except Exception as e:
			return Response({"detail":"Face cannot be detected in image"},status=401)

		result = None
		for person in os.listdir(self.images_base_path):
			known_face = face_recognition.load_image_file(os.path.join(self.images_base_path,person))
			try:
				known_encoding = face_recognition.face_encodings(known_face)[0]
				result  = face_recognition.compare_faces([known_encoding],unkown_encoded,tolerance=0.5)
				if (result):
					firstname,lastname = person.split('.')[0].split("_")
					break
			except Exception as e:
				pass
		if not result[0]:
			raise AuthenticationFailed(detail="Face provided has no match in our database")

		response = {
			"message":"Succesfully authentication",
			"result":result[0],
			"identity":f"{firstname} {lastname}"
		}
		
		return Response(response)


class Greatings(APIView):
	permission_classes = [permissions.AllowAny]

	def get(self,request):
		response = {
			"greatings":"Hellow"
		}
		return Response(response,status=200)
	