#Calculated according to 
class CalorieCalculator:
    def __init__(self):
        self.weightkg = 0.0
        self.heightcm = 0.0
        self.age = 0.0
        self.gender = 1  # 1 for male, 0 for female
        self.AMR = 1.2
        self.LAMR = [1.2, 1.375, 1.55, 1.725, 1.9]

    def WomenBMR(self):
        return (447.593
                + (9.247 * self.getWeight())
                + (3.098 * self.getHeight())
                - (4.330 * self.getAge()))

    def MenBMR(self):
        return (88.362
                + (13.397 * self.getWeight())
                + (4.799 * self.getHeight())
                - (5.677 * self.getAge()))

    def Questions(self):
        x = None
        while x != 'y' and x != 'Y':
            while (x != 1 and x != 0):
                x = int(input("Gender (1 for male, 0 for female): "))
                self.setGender(x)
                if (x != 1 and x != 0):
                    print("INVALID INPUT")
            x = int(input("Age in Years: "))
            self.setAge(x)
            x = float(input("Height in cm: "))
            self.setHeight(x)
            x = float(input("Weight in kg: "))
            self.setWeight(x)
            x = int(input("On a scale of 1-5: \n1.Little or no exercise \n2. 1-3 days a week \n3. 3-5 days a week \n4. 6-7 days a week \n5. hard exercise 6-7 days a week \nHow often do you exercise?: ")) - 1
            self.setAMR(x)
            x = input("Do your answers look right? Enter y or Y to confirm: ")
            

    def MaintenanceCalories(self):
        return self.getAMR() * self.getBMR()

    def getAMR(self):
        return self.AMR

    def getWeight(self):
        return self.weightkg

    def getHeight(self):
        return self.heightcm

    def getAge(self):
        return self.age

    def getGender(self):
        return self.gender

    def getBMR(self):
        if self.getGender() == 1:
            return self.MenBMR()
        else:
            return self.WomenBMR()

    def setWeight(self, x):
        self.weightkg = x

    def setHeight(self, x):
        self.heightcm = x

    def setAge(self, x):
        self.age = x

    def setAMR(self, x):
        self.AMR = self.LAMR[x]

    def setGender(self, x):
        self.gender = x

if __name__ == "__main__":
    cc = CalorieCalculator()
    cc.Questions()
    print("Your maintenance calories is:")
    print(cc.MaintenanceCalories())
