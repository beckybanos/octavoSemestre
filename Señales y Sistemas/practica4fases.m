%Gráficas
t = (0:0.001:2);
x = cos(2*pi*t);
y = cos(2*pi*t);

subplot(5,2,1);
plot(t,x,'r');
hold on;
plot(t,y,'b');
subplot(5,2,2);
plot(y,x);

x = cos(2*pi*t);
y = cos((2*pi*t)+(pi/4));

subplot(5,2,3);
plot(t,x,'r');
hold on;
plot(t,y,'b');
subplot(5,2,4);
plot(y,x);

x = cos(2*pi*t);
y = cos((2*pi*t)+(pi/2));

subplot(5,2,5);
plot(t,x,'r');
hold on;
plot(t,y,'b');
subplot(5,2,6);
plot(y,x);

x = cos(2*pi*t);
y = cos((2*pi*t)+(3*pi/4));

subplot(5,2,7);
plot(t,x,'r');
hold on;
plot(t,y,'b');
subplot(5,2,8);
plot(y,x);

x = cos(2*pi*t);
y = cos((2*pi*t)+(2*pi));

subplot(5,2,9);
plot(t,x,'r');
hold on;
plot(t,y,'b');
subplot(5,2,10);
plot(y,x);

