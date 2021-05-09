# Инкапсуляция — ограничение доступа к составляющим объект компонентам (методам и переменным).

# Python не имеет таких модификаторов , как private , protected , public . 
# Вы можете эмулировать их поведение с помощью __getattr__ и __getattribute__ 

class Phone:
    username = "Kate"                
    __how_many_times_turned_on = 0   

    def call(self):                  
        print( "Ring-ring!" )

    def __turn_on(self):             
        self.__how_many_times_turned_on += 1 
        print( "Times was turned on: ", self.__how_many_times_turned_on )

my_phone = Phone()

my_phone.call()
print( "The username is ", my_phone.username )