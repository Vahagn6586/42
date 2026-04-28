/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strncmp.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vrafyan <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/30 21:43:52 by vrafyan           #+#    #+#             */
/*   Updated: 2026/02/15 15:57:25 by vrafyan          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_strncmp(const char *s1, const char *s2, size_t n)
{
	size_t	i;

	if (!s1 || !s2)
		return (0);
	if (n == 0)
	{
		return (0);
	}
	i = 0;
	while ((*s1 + i) != '\0' && *(s2 + i) != '\0' && i < n - 1)
	{
		if (*(s1 + i) != *(s2 + i))
		{
			return ((unsigned char)*(s1 + i) - (unsigned char)*(s2 + i));
		}
		++i;
	}
	return ((unsigned char)*(s1 + i) - (unsigned char)*(s2 + i));
}
