clear all;
close all;
clc;

%非负矩阵分解
V = double(imread('pic.jpg'));
imshow(mat2gray(V));             %实现图像矩阵的归一化操作。所谓"归一化"就是使矩阵的每个元素的值都在0和1之间。0黑色，1白色。
[i,u] = size(V);
r = 100;                         %设置分解矩阵的秩
W = rand(i,r);                   %初始化WH，为非负数
H = rand(r,u);
max = 100;                       %最大迭代次数

for iter=1:max
    W = W.*((V./(W*H))*H');
    W = W./(ones(i,1)*sum(W));
    H = H.*(W'*(V./(W*H)));
end

img_V = W*H;
figure;
imshow(mat2gray(img_V));