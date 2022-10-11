from rest_framework import serializers 
from inmuebleslist_app.models import Empresa,Edificacion


# CORE ARGUMENTS
# class InmuebleSerializer (serializers.Serializer):  
#     class Meta:
#         model = Inmueble
#         fields = ["id","direccion","pais"]
    
class EmpresaSerializer (serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = "__all__"
        
class EdificacionSerializer (serializers.ModelSerializer):
    
    class Meta:
        model = Edificacion
        fields = "__all__"


# def column_longitud(value):
#         if len(value) <2:
#             raise serializers.ValidationError("El valor es demasiado corto")
    



    # id = serializers.IntegerField(read_only= True)
    # direccion = serializers.CharField(validators = [column_longitud])
    # ciudad = serializers.CharField(validators = [column_longitud])
    # CP = serializers.CharField()
    # pais = serializers.CharField()
    # activo = serializers.BooleanField(default=True)
    
    
    # def create(self, validated_data):
    #     return Inmueble.objects.create(**validated_data)
    
    # def update(self ,instance,validated_data):
    #     instance.direccion = validated_data.get('direccion',instance.direccion)
    #     instance.ciudad = validated_data.get('ciudad',instance.ciudad)
    #     instance.CP = validated_data.get('CP',instance.CP)
    #     instance.pais = validated_data.get('pais',instance.pais)
    #     instance.activo = validated_data.get('activo',instance.activo)
    #     instance.save()
    #     return instance
    
    
    # def validate (self, data):
    #     if data ['direccion'] == data['pais']:
    #         raise serializers.ValidationError('la direccion y el pais deben ser diferentes')
    #     else: 
    #         return data
        
    # def validate_imagen(self,data):
    #         if len(data) <2:
    #             raise serializers.ValidationError('el valor es muy corto')
    #         else: 
    #             return data



