def main():
    feedback = 'Алиса и Вася, большое спасибо за теплый приём!'
    a = feedback[0:5]    # срез Алисы
    b = feedback[8:12]   # срез Васи
    print(f"Назначить премию: {a}/{b}")
if __name__ == "__main__":
    main() 
