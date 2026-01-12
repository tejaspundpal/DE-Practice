Input = [
"/region//us-east-a/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.155.2/file_path//usr/bin/test1.csv",
"/region//us-east-b/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.156.2/file_path/teams/bin/test1.csv",
"/region//us-east-c/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.151.2/file_path/teams/bin/test1.csv",
"/region/japan/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.155.22/file_path/data/bin/test1.csv",
"/region/india/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.167.2/file_path//usr/bin/test1.csv",
"/region//us-east-a/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.179.28/file_path//usr/bin/test1.csv",
"/region//us-east-b/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.155.31/file_path/worklog/bin/test1.csv",
"/region//us-east-c/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.151.2/file_path//tmp/bin/test1.csv"
]

# Output:- ["10.168.155.2","10.168.156.2","10.168.151.2"
#            "10.168.155.22","10.168.167.2",
#            "10.168.179.28","10.168.155.31" ]

result = set()

for i in Input:
    # Split by '/server/' and take the part after, then split by '/' and take the first part (the IP)
    ip = i.split("/server/")[1].split("/")[0]
    result.add(ip)

print(result)


#question 2 
Input = ["mverma6250@gmail.com","ramesh02@hotmail.com",
        "sohansingh@gmail.com","swatirahane@outlook.com"]

# output = ["m********0@gmail.com","r******2@hotmail.com",
#         "s********h@gmail.com","s*********e@outlook.com"]

for email in Input:
    username, domain = email.split('@')
    username = username[0] + '*' * (len(username) - 2) + username[-1]
    print(f"\n{username}@{domain}")

