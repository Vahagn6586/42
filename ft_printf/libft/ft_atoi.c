/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_atoi.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vrafyan <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/02 14:24:21 by vrafyan           #+#    #+#             */
/*   Updated: 2026/02/12 20:05:58 by vrafyan          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_atoi(const char *str)
{
	int	sign;
	int	retval;

	sign = 1;
	retval = 0;
	while (*str == ' ' || (*str >= 9 && *str <= 13))
	{
		++str;
	}
	if (*str == '+' || *str == '-')
	{
		if (*str == '-')
			sign = -sign;
		++str;
	}
	while (*str >= '0' && *str <= '9')
	{
		retval = retval * 10 + (*str - '0');
		++str;
	}
	return (retval * sign);
}
