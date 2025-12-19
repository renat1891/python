from faker import Faker
fake = Faker("uk_UA")

print(fake.user_name())
print(fake.first_name())
print(fake.last_name())
print(fake.company())
print(fake.job())
print(fake.date_of_birth(minimum_age=18, maximum_age=60))
print(fake.url())
print(fake.ipv4())
print(fake.user_name())
print(fake.password(length=12, special_chars=True, digits=True, upper_case=True, lower_case=True))
