X = []
numImages = 0
for num=1:1000 % upto 1000 fonts; increase if needed

	filename = strcat('dataset/images/',strcat(num2str(num),'.png'));
	if ~exist(filename,'file')
		continue
	end
	disp(filename);
	image = imread(filename);
	for i=1:5
		for j=1:19
			k = (i - 1) * 30 + 1;
			l = (j - 1) * 30 + 1;
			X1 = reshape(image(k + 3:k + 32 , l : l + 29 , 1),1,900);
			X = [X ; X1];
		end
	end
	X = X(1:end - 3, :);
	numImages ++;
end
Y = repmat([1:92]',numImages,1);
dlmwrite('dataset/extract/x.csv',X)
dlmwrite('dataset/extract/y.csv',Y)
