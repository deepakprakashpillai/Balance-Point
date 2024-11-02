from pyexpat import model
from rest_framework.serializers import ModelSerializer,PrimaryKeyRelatedField
from .models import FoodItem,FoodServing,Meal

class FoodItemSerializer(ModelSerializer):
    class Meta:
        model = FoodItem
        fields = '__all__'
        

class FoodServingSerializer(ModelSerializer):
    food_item = PrimaryKeyRelatedField(queryset = FoodItem.objects.all(), write_only = True)
    class Meta:
        model = FoodServing
        fields = ['id','food_item','meal','quantity','note']
        extra_kwargs = {'meal': {'required': False}}
    def to_representation(self, instance):
        repr =  super().to_representation(instance)
        repr['food_item'] = FoodItemSerializer(instance.food_item).data
        return repr


class MealSerializer(ModelSerializer):
    food_servings = FoodServingSerializer(many=True)
    class Meta:
        model = Meal
        fields = ['id','user','date_time','total_calories','meal_experience','food_servings']
        
    def create(self, validated_data):
        meal_servings_data = validated_data.pop('food_servings')
        meal = Meal.objects.create(**validated_data)
        
        for servings_data in meal_servings_data:
            FoodServing.objects.create(meal=meal,**servings_data)
            
        return meal
    
    def update(self, instance, validated_data):

        instance.date_time = validated_data.get('date_time', instance.date_time)
        instance.meal_experience = validated_data.get('meal_experience', instance.meal_experience)
        instance.total_calories = validated_data.get('total_calories', instance.total_calories)
        instance.save()

        food_servings_data = validated_data.pop('food_servings', [])
        current_servings = {serving.id: serving for serving in instance.food_servings.all()}
        updated_serving_ids = [serving_data.get('id') for serving_data in food_servings_data if 'id' in serving_data]
        

        for serving_data in food_servings_data:
            serving_id = serving_data.get('id')
            
            if serving_id and serving_id in current_servings:

                serving_instance = current_servings[serving_id]
                for attr, value in serving_data.items():
                    setattr(serving_instance, attr, value)
                serving_instance.save()
            else:
                
                serving_data.pop('meal', None)
        
                FoodServing.objects.create(meal=instance, **serving_data)
        

        for serving_id, serving_instance in current_servings.items():
            if serving_id not in updated_serving_ids:
                serving_instance.delete()
        
        return instance
        