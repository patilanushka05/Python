def main():
    
    try:
        fobj = open("Demo.txt","r")
        print("File gets successfully open")

        Data=fobj.read()

        print("Data from file is: ",Data)

        fobj.close()

    except FileNotFoundError:
        print("Unable to file as there is no such file")

    finally:

        print("End of application")
        
if __name__=="__main__":
    main()