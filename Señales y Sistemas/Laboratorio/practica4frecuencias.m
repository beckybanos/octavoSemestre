%Frecuencias
t = (0:0.001:2);
x = cos(2*pi*t);
y = cos(2*pi*2*t);
z = cos((2*pi*2*t)+(pi/2));

subplot(3,3,1);
plot(t,x,'r');
hold on;
plot(t,y,'b');
subplot(3,3,2);
plot(x,y);
subplot(3,3,3);
plot(x,z);


x = cos(2*pi*t);
y = cos(2*pi*3*t);
w = cos((2*pi*t)+(pi/2));
z = cos((2*pi*3*t)+(pi/2));

subplot(3,3,4);
plot(t,x,'r');
hold on;
plot(t,y,'b');
subplot(3,3,5);
plot(x,y);
subplot(3,3,6);
plot(x,z);


x = cos(2*pi*t);
y = cos(2*pi*4*t);
w = cos((2*pi*t)+(pi/2));
z = cos((2*pi*4*t)+(pi/2));

subplot(3,3,7);
plot(t,x,'r');
hold on;
plot(t,y,'b');
subplot(3,3,8);
plot(x,y);
subplot(3,3,9);
plot(x,z);
