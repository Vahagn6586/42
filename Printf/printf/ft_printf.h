/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vchiling <vchiling@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/15 14:36:03 by vchiling          #+#    #+#             */
/*   Updated: 2026/03/16 18:11:26 by vchiling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FT_PRINTF_H
# define FT_PRINTF_H

# define F_MINUS 1
# define F_PLUS 2
# define F_SPACE 4
# define F_ZERO 8
# define F_HASH 16
# define IS_INT "diuxX"
# define CAP_BASE_16 "0123456789ABCDEF"
# define BASE_16 "0123456789abcdef"
# define BASE_10 "0123456789"

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

int			*ft_strchr(const char *str, char s);
size_t		ft_strlen(const char *s);
void		ft_putstr(const char *str);

#endif
