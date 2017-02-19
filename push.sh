
if [ $# -eq 0 ]; then
	echo "need commit message."
	exit
fi

git add -A
git commit -m $($1)
git push origin master

echo "done."