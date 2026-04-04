from typing import List
import matplotlib.pyplot as plt


class Person:
    def __init__(self,
                 title: str,
                 isFinanciallyLiterate: bool,
                 savings: int = 5000,
                 checking: int = 0,
                 salary: int = 61000,
                 debt: int = 30100,
                 debtInterest: float = 0.2,
                 savingspercent: float = 0.2,
                 checkingpercent: float = 0.3,
                 rent: int = 850,
                 houseprice: int = 175000,
                 mortgage_payments: int = 360):

        self.name = title
        self.FL = isFinanciallyLiterate

        self.savings = float(savings)
        self.checking = float(checking)
        self.salary = float(salary)
        self.debt = float(debt)
        self.debtInterest = float(debtInterest)
        self.savingspercent = float(savingspercent)
        self.checkingpercent = float(checkingpercent)

        self.has_house = False
        self.rent = float(rent)
        self.houseprice = float(houseprice)

        self.mortgage_payments_total = mortgage_payments
        self.mortgage_payments_left = mortgage_payments

        if self.FL:
            self.savingsReturn = 0.07
            self.additionalPay = 15
            self.mortgage_interest = 0.045
            self.downpayment = self.houseprice * 0.2
        else:
            self.savingsReturn = 0.01
            self.additionalPay = 1
            self.mortgage_interest = 0.05
            self.downpayment = self.houseprice * 0.05

        self.loan = self.houseprice - self.downpayment

    def __str__(self):
        return (
            f"Name: {self.name}\n"
            f"Financially Literate: {self.FL}\n"
            f"Savings: {self.savings}\n"
            f"Checking: {self.checking}\n"
            f"Debt: {self.debt}\n"
            f"Has House: {self.has_house}\n"
            f"Mortgage Payments Left: {self.mortgage_payments_left}"
        )

    def get_wealth(self):
        return int(self.savings + self.checking - self.debt - self.loan)

    def pay(self, amount):
        amount = min(amount, self.checking + self.savings)

        paid_from_checking = min(amount, self.checking)
        self.checking -= paid_from_checking

        remaining = amount - paid_from_checking
        paid_from_savings = min(remaining, self.savings)
        self.savings -= paid_from_savings

        return paid_from_checking + paid_from_savings

    def buy_house(self):
        if not self.has_house and self.checking + self.savings >= self.downpayment:
            self.pay(self.downpayment)
            self.has_house = True

    def checks(self):
        if not self.has_house and self.checking + self.savings >= self.downpayment:
            self.buy_house()

    def anual_tick(self):
        self.checks()

        self.checking += self.salary * self.checkingpercent
        self.savings += self.savings * self.savingsReturn
        self.savings += self.salary * self.savingspercent

        self.debt *= (1 + self.debtInterest)

        debt_paid_this_year = 0
        mortgage_paid_this_year = 0

        for _ in range(12):
            if not self.has_house:
                self.pay(self.rent)
            elif self.mortgage_payments_left > 0:
                r = self.mortgage_interest / 12
                n = self.mortgage_payments_left
                payment = self.loan * (r * (1 + r) ** n) / ((1 + r) ** n - 1)

                actual_payment = self.pay(payment)
                interest_portion = self.loan * r
                principal_paid = max(0, actual_payment - interest_portion)

                self.loan = max(0, self.loan - principal_paid)
                mortgage_paid_this_year += actual_payment

                if actual_payment > 0:
                    self.mortgage_payments_left -= 1

            if self.debt > 0:
                debt_payment_due = self.debt * 0.03 + self.additionalPay
                actual_debt_payment = self.pay(min(debt_payment_due, self.debt))
                self.debt = max(0, self.debt - actual_debt_payment)
                debt_paid_this_year += actual_debt_payment

        return debt_paid_this_year, mortgage_paid_this_year


class Simulation:
    def __init__(self, person: Person, years: int = 40):
        self.person = person
        self.years = years

        self.years_in_debt = 0
        self.total_debt_paid = 0
        self.total_mortgage_paid = 0

    def run(self):
        wealth_over_time = [self.person.get_wealth()]

        for _ in range(self.years):
            if self.person.debt > 0:
                self.years_in_debt += 1

            debt_paid, mortgage_paid = self.person.anual_tick()
            self.total_debt_paid += debt_paid
            self.total_mortgage_paid += mortgage_paid
            wealth_over_time.append(self.person.get_wealth())

        return wealth_over_time

    def summary(self) -> dict:
        return {
            "final_wealth": int(self.person.get_wealth()),
            "years_in_debt": int(self.years_in_debt),
            "total_debt_paid": int(self.total_debt_paid),
            "total_mortgage_paid": int(self.total_mortgage_paid)
        }


def plot_wealth(fl_wealth_history: List[float],
                nfl_wealth_history: List[float],
                filename: str = "wealth_over_time.png") -> None:
    plt.plot(fl_wealth_history, label="Financially Literate")
    plt.plot(nfl_wealth_history, label="Not Financially Literate")
    plt.title("Wealth Over Time")
    plt.xlabel("Years")
    plt.ylabel("Wealth ($)")
    plt.legend()
    plt.savefig(filename)
    plt.show()


def run_tests():
    p = Person("test", True)
    assert p.get_wealth() == int(p.savings + p.checking - p.debt - p.loan)

    p2 = Person("test2", False, checking=100, savings=50)
    paid = p2.pay(120)
    assert int(paid) == 120
    assert int(p2.checking) == 0
    assert int(p2.savings) == 30

    sim = Simulation(Person("sim", True), 5)
    history = sim.run()
    assert len(history) == 6

    summary = sim.summary()
    assert "final_wealth" in summary
    assert "years_in_debt" in summary
    assert "total_debt_paid" in summary
    assert "total_mortgage_paid" in summary
    
    print("all tests passed")


def main():
    run_tests()

    graham = Simulation(Person("graham", True), 40)
    movses = Simulation(Person("movses", False), 40)

    g = graham.run()
    m = movses.run()

    plot_wealth(g, m)

    summary_fl = graham.summary()
    summary_nfl = movses.summary()

    print(
        f"RESULT "
        f"fl_final_wealth={summary_fl['final_wealth']} "
        f"nfl_final_wealth={summary_nfl['final_wealth']} "
        f"fl_years_in_debt={summary_fl['years_in_debt']} "
        f"nfl_years_in_debt={summary_nfl['years_in_debt']} "
        f"fl_total_debt_paid={summary_fl['total_debt_paid']} "
        f"nfl_total_debt_paid={summary_nfl['total_debt_paid']} "
        f"fl_total_mortgage_paid={summary_fl['total_mortgage_paid']} "
        f"nfl_total_mortgage_paid={summary_nfl['total_mortgage_paid']}"
    )


if __name__ == "__main__":
    main()
    run_tests()