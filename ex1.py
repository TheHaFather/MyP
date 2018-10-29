class my(BaseException):
    def __init__(self,mess):
        super().__init__(mess)



class no(my):
    def validage(age):
        if age>18:
            print("cno must be 10 digits")
        else:
            raise my("not allowed")


    def cno(cno):
        if len(cno)==10:
            print("registration complete")
        else:
            raise my("10 digits")

    try:
        a = int(input("age:"))
        validage(a)
        b = input("cno:")
        cno(b)

    except my as me:
        print(me)
    finally:
        print("u r awesome")