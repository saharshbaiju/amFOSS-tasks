# TASK-11 : OVERTHEWIRE BANDIT

## MY EXPERIENCE

This task was really new to me except the basic linux commands which i learned from task-01 .By doing this task i learned new commands and ssh connectivity etc.
And even tough there was a learning curve the task was really engaging.
## Level 0

![alt text](images/image.png)

![alt text](images/image-1.png)

![alt text](images/image-2.png)

## Level 1

![alt text](images/image-3.png)

### Password

Password is - ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If

### Commands used

ls and cat

## Level 2

### Password

MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx

![alt text](images/image-5.png)

![alt text](images/image-6.png)

## Level 3

### Password

2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ

![alt text](images/image-7.png)

## Level 4

### Password

4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw

![alt text](images/image-8.png)

## Level 5

### Password

HWasnPhtq9AVKe0dmk45nxy20cvUa6EG

![alt text](images/image-9.png)

## Level 6

### Password

morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj

![alt text](images/image-10.png)

### Command Used

find / -user bandit7 -group bandit6 -size 33c 2>/dev/null

## Level 7

### Password

dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc

![alt text](images/image-11.png)

### Command Used

grep -i 'millionth' data.txt

## Level 8

### Password

4CKMh1JI91bUIZZPXDqGanal4xvAg0JM

![alt text](images/image-12.png)

### Command Used

sort data.txt | uniq -u

## Level 9

### Password

FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey

![alt text](images/image-13.png)

### Command Used

strings -a data.txt

## Level 10

### Password

The password is dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr

![alt text](images/image-14.png)

### Command Used

base64 -d data.txt

## Level 11

### Password

![alt text](images/image-15.png)

The password is 7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4

### Command Used

tr 'A-Za-z' 'N-ZA-Mn-za-m' < data.txt

## Level 12

### Password

![alt text](images/image-16.png)

The password is FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn

### Command Used

* gzib1
* gzib2
* xxd xf
* mkdir
* mv
* cat
* ls

## Level 13

### Password

MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS

![alt text](images/image-17.png)

### Command Used

ssh -i sshkey.private bandit14\@localhost

## Level 14

### Password

8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo

![alt text](images/image-18.png)

### Command Used

echo "MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS" | nc localhost 30000

## Level 15

### Password

kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx

![alt text](images/image-19.png)

### Command Used

echo "8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo" | ncat --ssl localhost 30001
