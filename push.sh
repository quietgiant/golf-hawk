
echo "commit message > "
read msg

git add -A
git commit -m $(msg)
git push origin master

echo "done."