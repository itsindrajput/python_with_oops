#WAP to ask the user to enter names of their 3 favourite movies and store them in the list.
"""
  movies = []
  movie1 = input("Enter your 1st favourite movies: ")
  movie2 = input("Enter your 2nd favourite movies: ")
  movie3 = input("Enter your 3rd favourite movies: ")

  movies.append(movie1)
  movies.append(movie2)
  movies.append(movie3)

  print(movies)
"""

"""
  movies = []
  movie = input("Enter your 1st favourite movies: ")
  movies.append(movie)
  movie = input("Enter your 2nd favourite movies: ")
  movies.append(movie)
  movie = input("Enter your 3rd favourite movies: ")
  movies.append(movie)

  print(movies)
"""

"""
  movies = []
  movies.append(input("Enter Your First Movie: "))
  movies.append(input("Enter Your Second Movie: "))
  movies.append(input("Enter Your Third Movie: "))
  print(movies)
"""


#WAP to check if a list contains a palindrome of elements. (Hint: use copy() method)
"""
  elements = [1, "abc", "abc", 1]
  copy_elements = elements.copy()
  copy_elements.reverse()

  if(copy_elements == elements):
    print("Palindrome")
  else:
    print("Not Palindrome")
"""