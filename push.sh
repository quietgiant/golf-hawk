
if [ $# -eq 0 ]; then
	echo "Need commit message."
	exit
fi

git add -A
git commit -m $1
git push origin master
