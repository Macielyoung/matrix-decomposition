clear all;
close all;
clc;

%�Ǹ�����ֽ�
V = double(imread('pic.jpg'));
imshow(mat2gray(V));             %ʵ��ͼ�����Ĺ�һ����������ν"��һ��"����ʹ�����ÿ��Ԫ�ص�ֵ����0��1֮�䡣0��ɫ��1��ɫ��
[i,u] = size(V);
r = 100;                         %���÷ֽ�������
W = rand(i,r);                   %��ʼ��WH��Ϊ�Ǹ���
H = rand(r,u);
max = 100;                       %����������

for iter=1:max
    W = W.*((V./(W*H))*H');
    W = W./(ones(i,1)*sum(W));
    H = H.*(W'*(V./(W*H)));
end

img_V = W*H;
figure;
imshow(mat2gray(img_V));