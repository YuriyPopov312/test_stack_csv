import csv


class Charges():  # Класс с константами.  
    VALUE_STANDART = 301.26  # Норматив.  
    VALUE_COUNTER = 1.52  # Коэффицент трансформации счетчика.  
    VALUE_UNKNOWN = "unknown"


class Subscribers():  # Класс Абоненты.  
    
    def __init__(self, number, accrual_code, previous_value=0.0, current_value=0.0):
        self.number = number
        self.accrual_code = accrual_code
        self.previous_value = float(previous_value)
        self.current_value = float(current_value)
        if self.accrual_code == "1":  # Рассчитываем значение "Начислено", исходя из типа начисления.  
            self.accured = Charges.VALUE_STANDART
        elif self.accrual_code == "2":
            self.accured = (self.current_value - self.previous_value) * Charges.VALUE_COUNTER
        else:
            self.accured = Charges.VALUE_UNKNOWN
        
        self.surname = Charges.VALUE_UNKNOWN
        self.street = Charges.VALUE_UNKNOWN
        self.home_number = Charges.VALUE_UNKNOWN
        self.flat_number = Charges.VALUE_UNKNOWN

    def sub_in_row(self):  # Метод вывода данных в нужной форме.  
        row = [f"{self.number}",f"{self.surname}",f"{self.street}",f"{self.home_number}",f"{self.flat_number}",f"{self.accrual_code}",f"{self.previous_value}",f"{self.current_value}",f"{'{:.2f}'.format(self.accured)}"]
        return row


class Homes(Subscribers):  # Класс Дома.  

    def home_in_row(self):  # Метод вывода данных в нужной форме. 
        row = [f"{self.number}",f"{self.street}",f"{self.home_number}",f"{'{:.2f}'.format(self.accured)}"]
        return row


if __name__=="__main__":
    subscriber_charges = []  # Список "Начисления абоненты".  
    number_sub = 1
    with open('абоненты.csv', encoding = "utf8") as File:
        reader = csv.reader(File, delimiter=';')
        for row in reader:
            try:
                sub = Subscribers(number_sub, row[5], row[6], row[7])  # Создаем экземпляр класса и задаем ему атрибуты. 
                sub.home_number = row[3]
                sub.flat_number = row[4]
                sub.surname = row[1]
                sub.street = row[2]
                subscriber_charges.append(sub.sub_in_row())  # Заполняем список.  
                number_sub += 1
            except:
                row[0]="№ строки"
                row.append("Начислено")
                subscriber_charges.append(row)

    myFile = open('Начисления_абоненты.csv', 'w', newline="")
    with myFile:
        writer = csv.writer(myFile, delimiter=';')
        writer.writerows(subscriber_charges)
    
    accruals_home = [] # Список "Начисления дома".  
    support_list = []
    number_home = 1
    with open('абоненты.csv', encoding = "utf8") as File:
        reader = csv.reader(File, delimiter=';')
        for row in reader:
            try:
                home = Homes(number_home, row[5], row[6], row[7])  # Создаем экземпляр класса и задаем ему атрибуты. 
                home.home_number = row[3]
                home.flat_number = row[4]
                home.street = row[2]
                accruals_home.append(home.home_in_row())  # Заполняем список.
                number_home += 1
            except:
                row = ["№ строки","Улица","№ дома","Начислено"]
                accruals_home.append(row)

        for i in range(1, len(accruals_home)-1):  # Считаем сумму начислений за дом.  
            if accruals_home[i][3] != 0:
                for j in range(2, len(accruals_home)):
                    if accruals_home[i][2] == accruals_home[j][2] and accruals_home[i][1] == accruals_home[j][1] and accruals_home[i][0] != accruals_home[j][0]:  # Проверяем совпадения улиц и домов.       
                        accruals_home[i][3] =  str('{:.2f}'.format(float(accruals_home[i][3]) + float(accruals_home[j][3])))  # В одну строку накапливаем сумму с таких же домов.  
                        accruals_home[j][3] =  0  # Начисление откуда сумма уже взята, обнуляем.  
                    else:
                        continue

        for i in accruals_home:  # Переписываем в вспомогательный список уникальные строки с накопленными суммами.  
            if i[3] != 0:
                support_list.append(i)

        for i in range(1, len(support_list)):  # Расставляем порядковые номера.  
            support_list[i][0] = str(i)

        accruals_home = support_list

    myFile = open('Начисления_дома.csv', 'w', newline="")
    with myFile:
        writer = csv.writer(myFile, delimiter=';')
        writer.writerows(accruals_home)