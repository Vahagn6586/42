/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vrafyan <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/05 17:39:59 by vrafyan           #+#    #+#             */
/*   Updated: 2026/02/12 22:02:01 by vrafyan          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static void	parameter_assignment(int *temp, int *n, int *val, int *size)
{
	*temp = *n;
	*size = 0;
	if (*temp <= 0)
	{
		++(*size);
		*val = -*temp;
	}
	else
	{
		*val = *temp;
	}
}

static void	size_calc(int val, int *size)
{
	while (val != 0)
	{
		++(*size);
		val /= 10;
	}
}

char	*ft_itoa(int n)
{
	int		temp;
	int		val;
	int		size;
	char	*ret_val;

	ret_val = "";
	if (n == INT_MIN)
		return (ft_strdup("-2147483648"));
	parameter_assignment(&temp, &n, &val, &size);
	size_calc(val, &size);
	ret_val = malloc(size + 1);
	if (!ret_val)
		return (NULL);
	ret_val[size] = '\0';
	while (size > 0)
	{
		--size;
		ret_val[size] = (val % 10) + '0';
		val /= 10;
		if (size == 0 && n < 0)
			ret_val[0] = '-';
	}
	if (n == 0)
		ret_val[0] = '0';
	return (ret_val);
}
