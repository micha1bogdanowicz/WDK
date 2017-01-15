#!/bin/bash

#pliki dodawane w parametrach
# Wymagane sa zainstalowane w systemie programy md5deep oraz ssdeep
# W Debianach: apt-get install md5deep ssdeep

apt-get install md5deep ssdeep
clear

l_arg="$#"

echo "Liczba Argumentow: " $l_arg

for arg in $@;do
echo ""
echo "md5deep dla pliku :" $arg
md5deep $arg
echo ""
echo "ssdeep dla pliku :" $arg
ssdeep $arg
done

