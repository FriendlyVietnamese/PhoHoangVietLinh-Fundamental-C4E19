3
�ri[	  �               @   s<   d dl T d dlmZmZ dd� Zdd� ZG dd� de�Zd	S )
�    )�*)�choices�randintc             C   s   dj | ||�S )Nz{0} - {1} - {2})�format)�a�b�c� r	   �EC:\Users\vtc00\Desktop\doc.txt\C4E19\WebModule\web2\models\service.py�so_do   s    r   c             C   s   dj | ||�S )Nz{0}, {1}, {2})r   )r   r   r   r	   r	   r
   �describe   s    r   c               @   sB   e Zd Ze� Ze� Ze� Ze� Z	e� Z
e� Ze� Ze� Ze� ZdS )�ServiceN)�__name__�
__module__�__qualname__Z
ImageField�imageZStringField�nameZIntField�yobZgender�phone�height�addressr   �infor	   r	   r	   r
   r   
   s   r   N)Zmongoengine�randomr   r   r   r   ZDocumentr   r	   r	   r	   r
   �<module>   s   