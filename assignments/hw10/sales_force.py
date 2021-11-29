"""
Name: Lexi Padberg
sales_force.py

Problem: this problem encapsulates data for a sales force

Certification of Authenticity: I certify that this assignment is entirely my own work
"""

from sales_person import SalesPerson


class SalesForce:
    ''' encapsulates data for a sales force '''
    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        infile = open(file_name, 'r')
        for line in infile:
            test_list = (line.split(","))
            em_id = test_list[0]
            name = test_list[1].strip()
            sales_data = test_list[2].strip()
            sales_data = (sales_data.split(" "))
            sales_data = [float(x) for x in sales_data]
            #print(sales_data)
            person = SalesPerson(em_id, name)
            for i in sales_data:
                person.enter_sale(i)
            self.sales_people.append(person)

    def quota_report(self, quota):
        quota_list = []
        for item in self.sales_people:
            em_id = item.get_id()
            name = item.get_name()
            total_sales = item.total_sales()
            quota_result = item.met_quota(quota)
            employee_list = [em_id, name, total_sales, quota_result]
            quota_list.append(employee_list)
        return quota_list

    def top_seller(self):
        top_sellers = []
        self.sales_people.sort(reverse=True, key=SalesPerson.total_sales)
        top_sellers.append(self.sales_people[0])
       # list(self.sales_people.split())
        for i in range(1, len(self.sales_people)):
            if self.sales_people[i].total_sales == top_sellers[0].total_sales:
                top_sellers.append(self.sales_people[i])
        return top_sellers

        #loopthrough the rest .. 1, len
        # compare each  index with sales[0]
        # if that results in 0, add them to sales
        # otherwise, stop loopinh
       # return sales

    def individual_sales(self, employee_id):
        for item in self.sales_people:
            if item.get_id() == employee_id:
                return item
        return None

if __name__ == "__main__":
    sf =SalesForce()
    sf.add_data("salesData.txt")
    print(sf.top_seller())
