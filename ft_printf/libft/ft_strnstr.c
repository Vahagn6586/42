/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strnstr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vrafyan <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/11 16:06:16 by vrafyan           #+#    #+#             */
/*   Updated: 2026/02/15 14:06:45 by vrafyan          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strnstr(const char *s1, const char *s2, size_t size)
{
	size_t	i;
	size_t	j;

	if (!s1 || !s2)
		return (NULL);
	if (*s2 == '\0')
		return ((char *)(s1));
	i = 0;
	while (s1[i] && i < size)
	{
		j = 0;
		while (s2[j] && s1[i] == s2[j] && s1[i] && i < size)
		{
			++i;
			++j;
		}
		if (s2[j] == '\0')
		{
			return ((char *)(s1 + i - j));
		}
		i = i - j + 1;
	}
	return (0);
}
