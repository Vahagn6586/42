/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vchiling <vchiling@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/15 14:36:03 by vchiling          #+#    #+#             */
/*   Updated: 2026/04/28 19:37:08 by vchiling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FT_PRINTF_H
# define FT_PRINTF_H

# define CAP_BASE_16 "0123456789ABCDEF"
# define BASE_16 "0123456789abcdef"
# define BASE_10 "0123456789"

# include "libft.h"
# include <limits.h>
# include <stdarg.h>
# include <stddef.h>
# include <stdint.h>
# include <stdlib.h>
# include <unistd.h>

typedef struct s_fspec
{
	char	fspec;
	int		(*handler)(va_list);
}			t_fspec;

int			handle_c(va_list args);
int			handle_p(va_list args);
int			handle_s(va_list args);
int			handle_x(va_list args);
int			handle_X(va_list args);
int			handle_u(va_list args);
int			handle_i_d(va_list args);
int			handle_percent(va_list args);

int			*ft_strchr(const char *str, char s);
size_t		ft_strlen(const char *s);
void		ft_putstr(const char *str);

#endif
