from faker import Faker

fake = Faker()

print(fake.name())

print(fake.address())

print(fake.text())

print(fake.unique.first_name())
print(fake.unique.last_name())

print(fake.word())
print(fake.building_number())
print(fake.prefix())
print(fake.suffix())

print(fake.simple_profile())
print(fake.date_of_birth())
print(fake.random_int(0, 20))

Faker.seed()
fake.country_calling_code()
print(fake.msisdn())
print(fake.phone_number())
