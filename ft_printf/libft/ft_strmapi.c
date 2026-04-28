/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strmapi.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vrafyan <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/11 16:11:42 by vrafyan           #+#    #+#             */
/*   Updated: 2026/02/15 14:35:20 by vrafyan          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strmapi(char const *s, char (*f)(unsigned int, char))
{
	int		i;
	int		size;
	char	*res;

	if (!s || !f)
	{
		return (NULL);
	}
	size = 0;
	i = 0;
	while (s[size])
	{
		++size;
	}
	res = malloc(size + 1);
	if (!res)
		return (NULL);
	while (i < size)
	{
		res[i] = f(i, s[i]);
		++i;
	}
	res[i] = '\0';
	return (res);
}
