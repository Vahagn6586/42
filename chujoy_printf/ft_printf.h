/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vrafyan <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/15 14:44:34 by vrafyan           #+#    #+#             */
/*   Updated: 2026/03/15 14:44:39 by vrafyan          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FT_PRINTF_H
# define FT_PRINTF_H
# include <stdarg.h>
# include <stddef.h>
# include <stdlib.h>
# include <unistd.h>

typedef int		(*t_handler)(va_list *args);

typedef struct t_identifier
{
	char		specifier;
	t_handler	func;
}				t_identifier;

char			*ft_itoa_base_up(unsigned long num, int base);
char			*ft_itoa_base_low(unsigned long num, int base);
int				ft_printf(const char *flag, ...);
int				ft_putnbr_unsigned(unsigned int n);
int				ft_putnbr(int n);
void			ft_putstr(const char *s);
size_t			ft_strlcpy(char *dest, const char *src, size_t size);
size_t			ft_strlen(const char *s);
int				handle_c(va_list *arg);
int				handle_int(va_list *arg);
int				handle_p(va_list *arg);
int				handle_s(va_list *arg);
int				handle_u(va_list *arg);
int				handle_x(va_list *arg);
int				handle_x_up(va_list *arg);
int				handle_per(va_list *arg);

#endif