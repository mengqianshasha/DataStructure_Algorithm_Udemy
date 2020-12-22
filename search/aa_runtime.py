from demo import *

# generate emails that contain the target email
list_of_domains = ['yaexample.com','goexample.com','example.com']
emails = generate_emails(10,list_of_domains,100000)

email = 'mengqianshasha@163.com'
emails.append(email)


sorted_emails = sorted(emails)

# run bisection search to look for the target email
index, found = binary_search(email, sorted_emails)
print(found)

if index:
    print(f'element at index {index} is {sorted_emails[index]}')

analyze_func(binary_search, email, sorted_emails)
analyze_func(generate_emails, 10, list_of_domains, 100000)



