#!/usr/bin/env bash


for FILE in ${BASE_PATH}/*; do 
	fname=`basename $FILE`
	echo "ln -s $FILE ${REZ_BUILD_PATH}/$fname"
	ln -s ${FILE} ${REZ_BUILD_PATH}/$fname
done

if [ "$1" == "install" ]; then
	for FILE in ${REZ_BUILD_PATH}/*; do
		fname=`basename $FILE`
		echo "cp -d ${FILE} ${REZ_BUILD_INSTALL_PATH}/$fname"
		cp -d ${FILE} ${REZ_BUILD_INSTALL_PATH}/$fname
	done
fi
