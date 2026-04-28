/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcpy.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vrafyan <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/01 22:05:44 by vrafyan           #+#    #+#             */
/*   Updated: 2026/02/15 14:17:32 by vrafyan          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

size_t	ft_strlcpy(char *dest, const char *src, size_t size)
{
	size_t	i;

	if (size == 0)
		return (ft_strlen(src));
	i = 0;
	while (*(src + i) != '\0' && i < size - 1)
	{
		*(dest + i) = *(src + i);
		++i;
	}
	*(dest + i) = '\0';
	while (*(src + i) != '\0')
		++i;
	return (i);
}
