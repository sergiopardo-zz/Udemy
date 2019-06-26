from message_user import MessageUser

def main():
    obj = MessageUser()
    obj.add_user("Justin", 123.32, "xerchpardo@gmail,com")
    obj.add_user("jOhn", 94.23)
    obj.add_user("Sean", 93.23)
    obj.add_user("Emilee", 193.23)
    obj.add_user("Marie", 13.23)
    print(obj.get_details())

    msg = obj.make_messages()
    print(msg)


if __name__ == "__main__":
    main()

    
