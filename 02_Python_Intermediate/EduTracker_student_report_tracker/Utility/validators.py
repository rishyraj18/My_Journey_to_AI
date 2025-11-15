class  validation:
    def validate_mark(value):
        if 0 < value >= 100:
            print("mark is valid")
        else:
            print("mark is invald")

    def validate_name(value):
        if value.istitle():
            print("This is Valid name")
        else:
            print("This is not a valid name")
        
    def validate_roll(value):
        if isinstance(value, int):
            print("Entred roll no is Valid")
        else:
            print("Invalid Roll no")