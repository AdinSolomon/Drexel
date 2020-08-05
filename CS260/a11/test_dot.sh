echo -e '5 3 1 2 7 6 8\nexample1.dot\n' | python3 make_dot.py
echo -e '5 3 1 4 7 6 8\nexample2.dot\n' | python3 make_dot.py
echo -e '9 8 7 6 5 4 3\nexample3.dot\n' | python3 make_dot.py
dot -Tjpg -oexample1.jpg example1.dot
dot -Tjpg -oexample2.jpg example2.dot
dot -Tjpg -oexample3.jpg example3.dot
