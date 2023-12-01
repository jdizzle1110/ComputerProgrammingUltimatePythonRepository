def meal_time(time):
  hour, minute = time.split(":")

  hour = int(hour)
  minute = int(minute)

  timenum = hour + minute/60

  if timenum >= 7 and timenum <= 11:
        return "Breakfast"
  elif timenum >= 12 and timenum <= 13:
        return "Lunch"
  elif timenum >= 18 and timenum <= 19:
        return "Dinner"
  else: 
        print ("Nothing right now")


print(meal_time("8:00"))
print(meal_time("12:00"))
print(meal_time("18:00"))

print("#################")

def get(data_file):
  filename, extension = data_file.split(".")
  return extension

print(get("hello.txt"))
print(get("data.cvs"))
print(get("data.json"))

print ("#################")


def is_image_file(filename):
  file, extensions = filename.split(".")
  if extensions == "jpg" or extensions == "png" or extensions == "jpeg" or extensions == "gif" or extensions == "tiff":
    return True 
  else:
    return False

print(is_image_file("hello.txt"))
print(is_image_file("data_cvs"))
print(is_image_file("dog.jpeg"))
print(is_image_file("hello.jpg"))
print(is_image_file("hello.png"))
print(is_image_file("hello.gif"))
print(is_image_file("hello.json"))

  
  


    
  