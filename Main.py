from App import App

def main():

    newApp = App()
    newApp.startDataBaseConnection()
    newApp.showWindow(newApp.VentanasIndex.LOGIN.value)
    newApp.stopApp()

    # 111.222.393-44 OFICIAL
    # 123.456.789-00 COMANDANTE
    # 555.666.797-88 CIENTISTA
    pass
    

if __name__ == "__main__":
    main()