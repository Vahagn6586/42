/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strchr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vrafyan <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/27 17:15:29 by vrafyan           #+#    #+#             */
/*   Updated: 2026/02/15 14:52:01 by vrafyan          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

const char	*ft_strchr(const char *str, int s)
{
	size_t	i;

	if (!str)
		return (NULL);
	i = 0;
	if (s == 0)
		return ((const char *)(str + ft_strlen(str)));
	while (*(str + i))
	{
		if (*(str + i) == (char)s)
		{
			return ((const char *)(str + i));
		}
		++i;
	}
	return (0);
}
