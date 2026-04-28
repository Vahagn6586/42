# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vchiling <vchiling@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/12 21:05:21 by vrafyan           #+#    #+#              #
#    Updated: 2026/04/28 19:35:10 by vchiling         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

CC = cc
CFLAGS = -Wall -Wextra -Werror

AR = ar
ARFLAGS = rcs

NAME = libftprintf.a libft.a

SRCS = ft_itoa_base.c ft_printf.c ft_putnbr.c ft_putnbr_unsigned.c ft_putstr.c ft_strlcpy.c \
ft_strlen.c handle_c.c handle_int.c handle_p.c handle_s.c handle_u.c handle_x.c handle_x_up.c ft_printf.c handle_per.c

OBJS = $(SRCS:.c=.o)

all: $(NAME) 

$(NAME): $(OBJS)
	$(AR) $(ARFLAGS) $@ $^

%.o: %.c ft_printf.h
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f $(OBJS)

fclean: clean
	rm -f $(NAME) test

re: fclean all

.PHONY: all clean fclean re test

