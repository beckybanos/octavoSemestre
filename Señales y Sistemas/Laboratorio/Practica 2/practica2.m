% % Comentarios
% t = linspace(-5,5,100); y = (exp(0.3*t)).*(sin(2*pi*t));
% 
% plot(t,y) 
% title ('Función exponencial compleja') 
% ylabel ('Amplitud')
% xlabel ('Tiempo') 
% grid on

f = [1,pi/8,pi/4,pi/2,pi,3*pi/2,7*pi/4,15*pi/8,2*pi];
subplot(3,3,1)
t = (0:1:30);
y = cos(t*f(1));
stem(t,y);
xlim([0,30]);
ylim([-1.5,1.5]);

subplot(3,3,2)
t = (0:1:30);
y = cos(t*f(2));
stem(t,y);
xlim([0,30]);
ylim([-1.5,1.5]);

subplot(3,3,3)
t = (0:1:30);
y = cos(t*f(3));
stem(t,y);
xlim([0,30]);
ylim([-1.5,1.5]);

subplot(3,3,4)
t = (0:1:30);
y = cos(t*f(4));
stem(t,y);
xlim([0,30]);
ylim([-1.5,1.5]);

subplot(3,3,5)
t = (0:1:30);
y = cos(t*f(5));
stem(t,y);
xlim([0,30]);
ylim([-1.5,1.5]);

subplot(3,3,6)
t = (0:1:30);
y = cos(t*f(6));
stem(t,y);
xlim([0,30]);
ylim([-1.5,1.5]);

subplot(3,3,7)
t = (0:1:30);
y = cos(t*f(7));
stem(t,y);
xlim([0,30]);
ylim([-1.5,1.5]);

subplot(3,3,8)
t = (0:1:30);
y = cos(t*f(8));
stem(t,y);
xlim([0,30]);
ylim([-1.5,1.5]);

subplot(3,3,9)
t = (0:1:30);
y = cos(t*f(9));
stem(t,y);
xlim([0,30]);
ylim([-1.5,1.5]);
