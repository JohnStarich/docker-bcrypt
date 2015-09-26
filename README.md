# docker-bcrypt
Create a bcrypt password quickly in Docker. Includes strength modifier and more!

## Try it
Just do the following to give it shot:
```
docker run --rm -it johnstarich/bcrypt -P
```
This will prompt you for a password and then hash it with a bcrypt generated salt at the default strength.

## Other options
All other options are documented in the container itself but here's an example using the "strength" modifier:
```
docker run --rm -it johnstarich/bcrypt -p "thing" -s 14
```
This hashes your password `thing` into something like `$2b$14$3s1Kkqo93Glpj92/vi9d2OBt0U.1Es2Y.Q7WAyoTAjrSUDwnG.4C6`
(the important part being the `$14$` near the beginning).

For usage, just run the container without any arguments like so:
```
docker run --rm -it johnstarich/bcrypt
```
