docker build --no-cache -t weather .
if [ $? -eq 0 ]; then
	docker run -i -t weather bash 
else
	echo "docker build failed please rerun"
fi 
