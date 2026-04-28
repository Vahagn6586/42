/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   utils.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vchiling <vchiling@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/15 15:42:13 by vchiling          #+#    #+#             */
/*   Updated: 2026/03/16 18:10:10 by vchiling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	*ft_strchr(const char *str, char s)
{
	char	i;

	i = 0;
	if (s == 0)
		return (0);
	while (*(str + i))
	{
		if (*(str + i) == (char)s)
		{
			return (1);
		}
		++i;
	}
	return (0);
}

size_t	ft_strlen(const char *s)
{
	int	i;

	i = 0;
	while (*(s + i))
		++i;
	return (i);
}

void	ft_putstr(const char *str)
{
	while (*str)
	{
		write(1, str, 1);
		++str;
	}
}
