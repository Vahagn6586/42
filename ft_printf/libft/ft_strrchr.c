/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strrchr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vrafyan <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/30 14:55:35 by vrafyan           #+#    #+#             */
/*   Updated: 2026/02/15 14:51:46 by vrafyan          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

const char	*ft_strrchr(const char *str, int ch)
{
	size_t	i;

	if (!str)
		return (NULL);
	i = 0;
	if (ch == 0)
	{
		return ((char *)(str + ft_strlen(str)));
	}
	while (str[i])
	{
		++i;
	}
	while (i--)
	{
		if (str[i] == (char)(ch))
		{
			return ((char *)(str + i));
		}
	}
	return (0);
}
