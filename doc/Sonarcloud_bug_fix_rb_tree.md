# SonarCloud bugfix - Red-Black Tree delete_fixup()
A SonarCloud egy bugot jelzett ennél a függvényél, miszerint a benne lévő loop csak egyszer fut le, és így felesleges a loop benne. 
Utánanéztem az algoritmusnak, és megtaláltam egy hasonló [implementációját](https://www.codesdope.com/course/data-structures-red-black-trees-deletion/), aminek a segítségével javítottam ezt.
Az [Issue#16](https://github.com/BME-MIT-IET/Brutal-Puppies-iet-2020/issues/16)-ban követhető ez a fix.
