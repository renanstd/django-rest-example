from rest_framework import serializers
from .models import Music, Band, Album, Member

class MusicSerializer(serializers.ModelSerializer):

    class Meta:

        model = Music
        fields = ('title', 'seconds', 'album')

class AlbumSerializer(serializers.ModelSerializer):

    class Meta:

        model = Album
        fields = ('title', 'band', 'date')

class BandSerializer(serializers.ModelSerializer):

    class Meta:

        model = Band
        fields = '__all__'

class MemberSerializer(serializers.ModelSerializer):

    class Meta:

        model = Member
        fields = ('name', 'age', 'band')
